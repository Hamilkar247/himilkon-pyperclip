console.log("pomiar_nowy.js")
let number_of_pomiar=null
let destinationURL=null
let regex = null

function func_for_number_of_pomiar(){
  let url = window.location.href
  table_of_url = url.split('/')
  console.log("table of url" + table_of_url)
  if (table_of_url[table_of_url.length - 1] == '') {
    number_of_pomiar = table_of_url[table_of_url.length - 2]
  }
  else {
    number_of_pomiar = table_of_url[table_of_url - 1]
  }
  console.log("url:"+window.location.href)
  console.log("number_of_pomiar:"+number_of_pomiar)
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
let start_owner=''
let start_czyWazny=''
let start_wartosc=''
let start_data_pomiaru=''

//wysywaleni danych na serwer
$("#form_zapis_pomiar").on("submit", function(e) {
   // obsluguje zdarzenie hoover czy submit - w tym przykladzie submit
   // efekt jest taki ze wywolanie submit nie skutkuje przeladowaniem strony, ktorym to submit domyslnie skutkuje
   e.preventDefault()
   console.log("form_zapis_pomiar")

   start_owner="arek" // do zmiany !
   start_czyWazny=$("#czyWazny").val()
   start_wartosc=$("#wartosc").val()
   start_data_pomiaru="2020-11-04T13:06:12.757407Z"//$("#data_pomiaru").val()
   console.log("owner: " + start_owner)
   console.log("czyWazny: " + start_czyWazny)
   console.log("wartosc: " + start_wartosc)
   console.log("data_pomiaru: " + start_data_pomiaru)
   destinationURL = get_urls().url_home + get_urls().api_v1_pomiar
   console.log("current url:" + destinationURL)
   $.ajax({
      url      : destinationURL,
      type     : "POST",
      data     : {
        //  owner:        start_owner,
          czyWazny:     start_czyWazny,
          wartosc:      start_wartosc,
        //  data_pomiaru: start_data_pomiaru,
          csrfmiddlewaretoken: csrftoken,
      },
   }).done(function(response) {
         alert('Save data');
   }).fail(function() {
         alert("Wystąpił błąd w połączeniu z djangorestapi")
   }).then(function() {
         console.log("owner: " + start_owner);
         console.log("czyWazny: " + start_czyWazny);
         console.log("wartosc: " + start_wartosc);
         console.log("data_pomiaru: " + start_data_pomiaru);
   })
})
