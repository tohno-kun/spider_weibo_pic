function getXHR() {
    var xhr = 0;
    try {
        xhr = new XMLHttpRequest()
    } catch (err1) {
        try {
            xhr = new ActiveXObject('Microsoft.XMLHTTP');
        } catch (err2) {
            try { xhr = new ActiveXObject('Msxml2.XMLHTTP') } catch (err3) {};
        }
    };
    return xhr;
};
var xhr = getXHR();
if (!xhr) {
    alert('您的浏览器版本过低，不支持XMLHttpRequest，请升级浏览器！');
};
xhr.onreadystatechange = function () {
    var data = xhr.responseText;
    console.log(data);
};
xhr.open("GET", 'https://github.com/tohno-kun/spider_weibo_pic/', true);
xhr.send(null);
