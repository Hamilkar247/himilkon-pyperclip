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

$(document).ready(function() {
    $('#dataTable').dataTable( {
      //  "order": [[ 3, "desc" ]]
    });
});

//uzupelnianie liste organizacji
$( document ).ready(function() {

    //console.log(window.location.href)
    //var url = new URL(window.location.href);
    //var organizacja = url.searchParams.get("organizacja");
    //console.log("organizacja: "+ organizacja);

   console.log("Window on load end")
   $.ajax({
       url: "http://127.0.0.1:8000/api/v1/organizacje/",
       type: "GET",
   }).done(function (response) {
       for(i=0; i<response.length; i++){
           console.log(response[i].id)
            console.log('<a href="/front/organizacje/' + response[i].id + '" class="btn btn-w-m btn-success"  >' + response[i].nazwa + '</a>');
           $('#organization_table').append(
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
   }).then(
     $('#mytable').dataTable( {
        //"order": [[ 3, "desc" ]]
     })
   )
})

$(document).ready(function() {
    $('#example').DataTable( {
        ajax: {
         url:  "http://127.0.0.1:8000/api/v1/organizacje/",
         type: "GET",
         dataSrc: "",
        },
        columns: [
            { data: 'id' },
            { data: 'nazwa' },
            { data: 'opis' }
        ]
    } );
} );

//wartosci z bazy danych pewnej organizacji
$(document).ready(function(){
   console.log("")
})

