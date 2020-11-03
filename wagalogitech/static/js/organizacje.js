function changeParagraph() {
  console.log("Juzue")
  document.getElementById("paragraphId").innerHTML = "static/js/Paragraph changed.";
}

function refreshPage() {
  window.location.reload();
}

//testowa funkcja jquery
$(document).ready(function(){
  $("#hideclick").click(function(){
    $(this).hide();
  })
})