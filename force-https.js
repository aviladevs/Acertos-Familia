(function(){
  try {
    var host = window.location.hostname;
    var proto = window.location.protocol;
    var isLocal = /^localhost$|^127\.0\.0\.1$/.test(host);
    var isFile = proto === 'file:';
    if (!isLocal && !isFile && proto !== 'https:') {
      var newUrl = 'https:' + window.location.href.substring(proto.length);
      window.location.replace(newUrl);
    }
  } catch (e) {
    // silent
  }
})();
