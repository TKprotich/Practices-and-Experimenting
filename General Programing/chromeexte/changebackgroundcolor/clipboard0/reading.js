const btn = document.querySelector("#reading")
// window.addEventListener('keyup', => )
btn.addEventListener('mousedown', readerScript() )
function readerScript(){
  window.location.href = "http://127.0.0.1:3000/"
}
