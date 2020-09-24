document.querySelector('#newtask').onkeyup = function () {
    if (document.querySelector('#newtask').value === '') {
        document.querySelector('#submit').disabled = true;
        document.querySelector('#reset').disabled = true;
        document.querySelector('#refresh').disabled = false;

    } else {
        document.querySelector('#submit').disabled = false;
        document.querySelector('#reset').disabled = false;
        document.querySelector('#refresh').disabled = true;
    }
}
document.querySelector('#reset').onclick = function () {
    document.querySelector('#submit').disabled = true;
    document.querySelector('#reset').disabled = true;
    document.querySelector('#refresh').disabled = false;
}