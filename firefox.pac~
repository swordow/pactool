
var strProxy = "SOCKS5 127.0.0.1:7070;SOCKS 127.0.0.1:7070";

function regExpMatch(url, patter)
{
  try {
    return new RegExp(pattern).test(url);
  } catch (ex) {
    return false;
  }
}

function FindProxyForURL(url, host)
{
  if (shExpMatch(url, "http*://*.google.com*")) return strProxy;
  if (shExpMatch(url, "http*://*.youtube.com*")) return strProxy;
  if (shExpMatch(url, "http*://*.youtube.com*") || shExpMatch(url, "http*://youtube.com*")) return strProxy;
	if (shExpMatch(url, "http*://*.youtubecn.com*") || shExpMatch(url, "http*://youtubecn.com*")) return strProxy;
  if (regExpMatch(url, "^https?:\\/\\/[^\\/]+google\\.(.*)")) return strProxy;
  if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?gmail\\.com"))  return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?google-analytics\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googleadservices\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googleapis\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googleearth\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googlecode\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googledrive\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googlehosted\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googlelabs\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googlemail\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googleplus\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googlesource\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googlesyndication\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googletagmanager\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googletagservices\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googleusercontent\\.com")) return strProxy;
	if (regExpMatch(url, "^[\\w\\-]+:\\/+(?!\\/)(?:[^\\/]+\\.)?googlevideo\\.com")) return strProxy;
  else return "DIRECT";
}
