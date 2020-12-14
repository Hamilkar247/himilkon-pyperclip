console.log("organizacja_detail.js")
let number_of_organizacja=null
let destinationURL=null
let regex = null
function func_for_number_of_organizacje(){
  let url = window.location.href
  table_of_url = url.split('/')
  console.log("table of url" + table_of_url)
  if (table_of_url[table_of_url.length - 1] == '') {
    number_of_organizacja = table_of_url[table_of_url.length - 2]
  }
  else {
    number_of_organizacja = table_of_url[table_of_url - 1]
  }
  console.log("url:"+window.location.href)
  console.log("number_of_organizacja:"+number_of_organizacja)
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


// zmienne przechowują dane przeslane z get
let start_nazwa_org=''
let start_opis_org=''


//wartosci z bazy danych pewnej organizacji
$(document).ready(function() {
   func_for_number_of_organizacje()
   console.log("jestesmy w szczegolach organizacji")
   destinationURL = get_urls().url_home + get_urls().api_v1_organizacje +number_of_organizacja
   console.log("current url:" + destinationURL)
   $.ajax({
      url: destinationURL,
      type: "GET",
   }).done(function(response) {
       console.log("udalo sie polaczyc przez ajaksa !")
       $('#nazwa_organizacji').attr('value', response.nazwa);
       $("#opis_organizacji").attr('value', response.opis);
   }).fail(function() {
     alert("Wystąpił błąd w połączeniu z djangorestapi!");
   }).then(function() {
     start_nazwa_org=$("#nazwa_organizacji").val()
     console.log("start_nazwa_org:" + start_nazwa_org)
     start_opis_org=$("#opis_organizacji").val()
     console.log("start_opis_org:" + start_opis_org)
   })
})

function deleteOrganization() {
  //e.preventDefault()
  console.log("funkcja DELETE Ajax")
  console.log("destinationURL:" + destinationURL)
  console.log("Numer elementu:"+ number_of_organizacja)
  $.ajax({
    url:  destinationURL,
    type: "DELETE",
    beforeSend: function(xhr) {
        xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    },
  }).done(function(response) {
    console.log("udalo sie usunąć element")
    alert("Usunąłeś element organizacji!")
  }).fail(function() {
    alert("Wystąpił błąd w połączeniu z djangorestapi!")
  }).then(function() {

  })
}
