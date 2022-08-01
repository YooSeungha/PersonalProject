function check(){
    var namevalOld = f.name.value;
    nameval = trim(namevalOld);
    if(nameval.length == 0){
        alert("이름을 넣어주세요");
        f.name.value = "";
        f.name.focus();
        return false;
    }else{
        pass = checkByteLen(namevalOld, 20);
        if(!pass){
            alert("이름이 너무 길어요");
            f.name.focus();
            return false;
        }
    }
    var addrvalOld = f.addr.value;
    addrval = trim(addrvalOld);

    if(addrval.length == 0){
        alert("주소를 넣어주세요");
        f.addr.value = "";
        f.addr.focus();
        return false;
    }else{
        pass = checkByteLen(addrvalOld, 20);
        if(!pass){
            alert("주소가 너무 길어요");
            f.addr.focus();
            return false;
        }
    }

    f.submit();
}

function checkByteLen(str, size){
    var byteLen = getByteLen(str);
    if(byteLen <= size){
        return true;
    }else{
        return false;
    }
}
function getByteLen(str){
   return str.replace(/[\0-\x7f]|([0-\u07ff]|(.))/g,"$&$1$2").length;
}

function enterCheck(elm){
    if(event.keyCode == 13){
        if(elm == f.name){
            f.addr.focus();
        }else{
            check();
        }
    }
}