function changeParagraph() {
  document.getElementById("paragraphId").innerHTML = "js/Paragraph changed.";
  var a=4;
  //console.clear()
  console.log("hejo ho changeParagraph" + str(a))
}

$(document).ready(function()){
  $("button").click(function(){
    $("p").hide();
  })
  console.log("hejo ho !")
}

/*
var URL= "/api/";

$(document).ready(
 function() {
   $("#organizacje").hide();
 }
);

function getOrganizacje()
{
  $.getJSON(URL,{},showOrganizacja);
}

function getCourser()
{
 $.getJSON(URL + $("#code").val())
 .done(showOrganizacja) //on sucess - 200
 .fail(function() // on failure - 404
    {
      alert("Sorry! Organizacja Not found!");
    }
}

function showOrganizacja(organizacja)
{
  $("#id").val(organizacja.id)
  $("#nazwa").val(organizacja.nazwa)
  $("#opis").val(organizacja.opis)
}

function showOrganizacja(organizacje)
{
  $("organizacjarows").html("")
  $.each(organizacje,
     function(idx, organizacja) {
       $("#organizacjarows").append(
       "<tr><td>" + organizacja.id + "</td>><td>" +
       organizacja.nazwa + "</td><td>" +
       organizacja.opis + "</td><td>");
     } //anonymous function
  ); //each()

  $("#organizacje".show();
} //showOrganizacje

function addOrganizacja()
{
  $.ajax(
   { "url": URL,
     "data": {
           "nazwa" : $("#nazwa").val(),
           "opis" : $("#opis").val()
     }
   }
  )
}

function add_success()
{
 alert("Added organizacje Successfully");
}

function add_error()
{
 alert("Could not add organizacja!");
}

function deleteOrganizacja()
{
 $.ajax(
  { "url": URL + $("#nazwa").val(),
    "type": "delete",
    "success" : delete_success,
    "error" : delete_error
  }; //ajax()
}

function delete_success()
{
 alert("Deleted Organizacja Successfully");
}

function delete_error()
{
 alert("Could not delete Organizacja'!");
}

function updateCourse()
{
   $.ajax(
      {  "url"     : URL + $("#opis").val() + "/",
         "data"    : { "nazwa"     : $("#nazwa").val(),
                       "opis"    : $("#opis").val(),
                      },
         "type"    : "put",
         "success" : update_success,
         "error"   : update_error
      }
  ); // ajax()
}

function update_success()
{
  alert("Updated Course Successfully");
}

function update_error()
{
  alert("Could not update Course!");
}
*/


/*
$( document ).ready(function() {
    console.log(window.location.href)
    var url = new URL(window.location.href);
    var organizacja = url.searchParams.get("organizacja");
    console.log("organizacja:" + organizacja);
    console.log("Window on load end");
    $.ajax({
        url: "/api/zlecenie/"+ancestor+"/zlecone_badania",
        type:"GET",
    }).done(function (response) {
        for(i=0; i<response.length; i++){
            console.log(response[i].id)
           $('#mytable tbody').append(
            '<tr>' +
                '<td>' + response[i].id + '</td>' +
                '<td>' + response[i].nazwa + '</td>' +
                '<td>' + response[i].opis + '</td>' +
                '<td><button id="btn_organizacja" + response[i].id'" class="btn btn-w-m btn-success" onclick="buttonFunction(this)"
                data-id="'+response[i].id+'">Utwórz badanie</button>+ '</td>+
            '</tr>');
        }
    })
});

function buttonFunction(obj){
  console.log("button function!")
}
*/