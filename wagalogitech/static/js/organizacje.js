function changeParagraph() {
  console.log("Juzue");
  document.getElementById("paragraphId").innerHTML = "static/js/Paragraph changed.";
}

function refreshPage() {
  window.location.reload();
}

//testowa funkcja jquery
$(document).ready(function(){
  $("#hideclick").click(function(){
    $("#hideclick").hide();
    console.log("znikniecie paragrafu hideclick");
  })
 console.log("zaladowano funkcje paragrafu hideclick");
})



//testowa funkcja ajaxa - jak wstawić ?
//$(document).ready(function(){
//  $("#przycisk").click(function(){
//    $.ajax({url: "static/js/demo_test.txt", success:
//      function(result){
//        $("#div1").html(result)}
//    });
//  })
//})

$( document ).ready(function() {

    //console.log(window.location.href)
    //var url = new URL(window.location.href);
    //var organizacja = url.searchParams.get("organizacja");
    //console.log("organizacja: "+ organizacja);

   console.log("Window on load end")
   $.ajax({
       url: "http://127.0.0.1:8000/api/organizacje/",
       type: "GET",
   }).done(function (response) {
       for(i=0; i<response.length; i++){
           console.log(response[i].id)
            console.log('<a href="/front/organizacje/' + response[i].id + '" class="btn btn-w-m btn-success"  >' + response[i].nazwa + '</a>');
           $('#mytable').append(
           '<tr>' +
               '<td>' + response[i].id + '</td>' +
               '<td>' + response[i].nazwa + '</td>' +
               '<td>' + response[i].opis + '</td>' +
               '<td>' +
                 '  <a href="/front/organizacje/' + response[i].id + '" class="btn btn-w-m btn-success">' + response[i].nazwa + '</a>' +
               '</td>' +
               //'<td><button id="btn_organizacja_'+response[i].id+'" class="btn btn-w-m btn-success"
               //onclick="buttonFunction(this)" data-id="'+response[i].id+'">Utwórz organizacje</button>'+
               //'</td>' +
           '</tr>');
       }
   }).fail(function() {
     alert("Wystapil blad w polaczeniu z djangorestapi!");
   })
})

//to nie wiem co u tomka za bardzo za co odpowiada
//function buttonFunction(obj){
//    zlecone_badanie_id = obj.getAttribute('data-id')
//    console.log()
//    location.href=='/admin/Procedura/etap_probka/add/?zlecone_badanie='+zlecone_badanie_id
//}


//$(document).ready(function()){
//  $("#butt").click(function(){
//    //$("#leftPanel").hide();
//    $("#hideclick").hide();
//    $(this).hide();
//  })
//  console.log("schowano left panel")
//}