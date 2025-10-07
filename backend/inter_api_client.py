import os
from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests

try:
    # Permite usar .pfx diretamente sem converter para PEM
    from requests_pkcs12 import Pkcs12Adapter  # type: ignore
except Exception:  # pragma: no cover
    Pkcs12Adapter = None  # type: ignore


@dataclass
class InterAPIConfig:
    base_url: str
    # Opção 1: PFX
    pkcs12_path: Optional[str] = None
    pkcs12_password: Optional[str] = None
    # Opção 2: PEM (cert + key)
    cert_pem: Optional[str] = None
    key_pem: Optional[str] = None
    # OAuth2 Client Credentials (opcional, alguns produtos exigem)
    token_url: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    scope: Optional[str] = None
    # Timeout padrão
    timeout: int = 30

    @staticmethod
    def from_env() -> "InterAPIConfig":
        return InterAPIConfig(
            base_url=os.getenv("INTER_API_BASE", "https://api.bancointer.com.br"),
            pkcs12_path=os.getenv("INTER_API_PFX"),
            pkcs12_password=os.getenv("INTER_API_PFX_PASSWORD"),
            cert_pem=os.getenv("INTER_API_CERT_PEM"),
            key_pem=os.getenv("INTER_API_KEY_PEM"),
            token_url=os.getenv("INTER_API_TOKEN_URL"),
            client_id=os.getenv("INTER_API_CLIENT_ID"),
            client_secret=os.getenv("INTER_API_CLIENT_SECRET"),
            scope=os.getenv("INTER_API_SCOPE"),
            timeout=int(os.getenv("INTER_API_TIMEOUT", "30")),
        )


class InterAPIClient:
    def __init__(self, cfg: Optional[InterAPIConfig] = None) -> None:
        self.cfg = cfg or InterAPIConfig.from_env()
        self.session = requests.Session()
        self._token: Optional[str] = None

        # Configura client auth mTLS
        if self.cfg.pkcs12_path and self.cfg.pkcs12_password:
            if Pkcs12Adapter is None:
                raise RuntimeError(
                    "requests_pkcs12 não instalado. Adicione ao requirements e configure o PFX ou converta para PEM."
                )
            self.session.mount(
                "https://",
                Pkcs12Adapter(
                    pkcs12_filename=self.cfg.pkcs12_path,
                    pkcs12_password=self.cfg.pkcs12_password,
                ),
            )
        elif self.cfg.cert_pem and self.cfg.key_pem:
            self.session.cert = (self.cfg.cert_pem, self.cfg.key_pem)
        else:
            raise RuntimeError(
                "Configure INTER_API_PFX + INTER_API_PFX_PASSWORD ou INTER_API_CERT_PEM + INTER_API_KEY_PEM"
            )

        # Cabeçalhos padrão
        self.session.headers.update({
            "Accept": "application/json",
            "User-Agent": "AvilaTransportes/1.0",
        })

    # =============
    # OAuth2 Token
    # =============
    def _ensure_token(self) -> None:
        if not self.cfg.token_url or not self.cfg.client_id or not self.cfg.client_secret:
            return  # OAuth2 não configurado
        if self._token:
            self.session.headers.setdefault("Authorization", f"Bearer {self._token}")
            return
        auth = (self.cfg.client_id, self.cfg.client_secret)
        data = {"grant_type": "client_credentials"}
        if self.cfg.scope:
            data["scope"] = self.cfg.scope
        resp = self.session.post(self.cfg.token_url, data=data, auth=auth, timeout=self.cfg.timeout)
        resp.raise_for_status()
        token = resp.json().get("access_token")
        if not token:
            raise RuntimeError("Token OAuth2 não retornado pela API do Inter")
        self._token = token
        self.session.headers["Authorization"] = f"Bearer {token}"

    def _url(self, path: str) -> str:
        base = self.cfg.base_url.rstrip("/")
        path = path if path.startswith("/") else f"/{path}"
        return f"{base}{path}"

    def get(self, path: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        url = self._url(path)
        self._ensure_token()
        resp = self.session.get(url, params=params, timeout=self.cfg.timeout, headers=headers)
        resp.raise_for_status()
        return resp

    def post(self, path: str, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        url = self._url(path)
        self._ensure_token()
        resp = self.session.post(url, json=json, timeout=self.cfg.timeout, headers=headers)
        resp.raise_for_status()
        return resp

    def put(self, path: str, json: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        url = self._url(path)
        self._ensure_token()
        resp = self.session.put(url, json=json, timeout=self.cfg.timeout, headers=headers)
        resp.raise_for_status()
        return resp

    def delete(self, path: str, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        url = self._url(path)
        self._ensure_token()
        resp = self.session.delete(url, timeout=self.cfg.timeout, headers=headers)
        resp.raise_for_status()
        return resp

    # Exemplos de wrappers (ajuste os caminhos conforme sua doc do Inter)
    def obter_saldo(self) -> Dict[str, Any]:
        # Exemplo genérico; ajuste path conforme sua documentação
        return self.get("/banking/v2/saldo").json()

    def obter_extrato(self, data_inicio: str, data_fim: str) -> Dict[str, Any]:
        params = {"dataInicio": data_inicio, "dataFim": data_fim}
        return self.get("/banking/v2/extrato", params=params).json()

    # =====
    # PIX
    # =====
    def pix_criar_cobranca(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        headers = {"Content-Type": "application/json"}
        return self.post("/pix/v2/cob", json=payload, headers=headers).json()

    def pix_consultar_cobranca(self, txid: str) -> Dict[str, Any]:
        return self.get(f"/pix/v2/cob/{txid}").json()

    def pix_criar_qrcode(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return self.post("/pix/v2/qr-code", json=payload).json()

    def pix_listar(self, inicio: str, fim: str, cpf_cnpj: Optional[str] = None) -> Dict[str, Any]:
        params: Dict[str, Any] = {"inicio": inicio, "fim": fim}
        if cpf_cnpj:
            params["txid"] = cpf_cnpj  # ajuste conforme filtros suportados
        return self.get("/pix/v2/pix", params=params).json()

    def pix_devolver(self, e2eid: str, devolucao_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        return self.put(f"/pix/v2/pix/{e2eid}/devolucao/{devolucao_id}", json=payload).json()

    def pix_webhook_registrar(self, chave: str, url: str) -> Dict[str, Any]:
        return self.put(f"/pix/v2/webhook/{chave}", json={"webhookUrl": url}).json()

    def pix_webhook_consultar(self, chave: str) -> Dict[str, Any]:
        return self.get(f"/pix/v2/webhook/{chave}").json()

    def pix_webhook_remover(self, chave: str) -> None:
        self.delete(f"/pix/v2/webhook/{chave}")

    # =========
    # BOLETOS
    # =========
    def boleto_emitir(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        return self.post("/cobranca/v2/boletos", json=payload).json()

    def boleto_consultar(self, nosso_numero: str) -> Dict[str, Any]:
        return self.get(f"/cobranca/v2/boletos/{nosso_numero}").json()

    def boleto_pdf(self, nosso_numero: str) -> bytes:
        # Conteúdo binário (PDF)
        resp = self.get(f"/cobranca/v2/boletos/{nosso_numero}/pdf")
        return resp.content

    def boleto_baixa(self, nosso_numero: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        # Ajuste o verbo/path conforme a doc (algumas versões usam POST, outras PUT)
        return self.post(f"/cobranca/v2/boletos/{nosso_numero}/baixa", json=payload).json()

