
window.onload = function(){
    var hw = document.getElementById('hw');
    hw.reaFileSync('sample.txt','utf8');
    hw.addEventListener('click', function(){
        console.log(text);
    })
}
