console.log("pomiar_nowy.js")
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
   //jeszcze inny sposób tablicowy
   //var data = {};
   //data.nazwa = $("#nazwa_organizacji").val()
   //data.opis = $("#opis_organizacji").val()

   $.ajax({
      url      : "http://127.0.0.1:8000/api/v1/pomiary",
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
  //alternatywna wersja wyswietlania danych w zapisie poza ajaxem
  ///.done(function(response){
  ///     console.log("nazwa org:"+ nazwa)
  ///     console.log("opis org:" + opis)
  ///}).fail(function() {
  ///    console.log("nazwa org:"+ nazwa)
  ///    console.log("opis org:" + opis)
  ///    alert("Wystąpił błąd w połaczeniu z DjangoRestApi")
  ///})

})
