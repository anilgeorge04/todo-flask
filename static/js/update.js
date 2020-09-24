document.querySelector('#updtask').onkeyup = function () {
    if (document.querySelector('#updtask').value === '') {
        document.querySelector('#submit').disabled = true;
        document.querySelector('#reset').disabled = true;

    } else {
        document.querySelector('#submit').disabled = false;
        document.querySelector('#reset').disabled = false;
    }
}
document.querySelector('#reset').onclick = function () {
    document.querySelector('#submit').disabled = true;
    document.querySelector('#reset').disabled = true;
}