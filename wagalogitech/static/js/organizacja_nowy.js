console.log("organizacja_nowy.js")
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

//wysywaleni danych na serwer
$("#form_zapisorg").on("submit", function(e) {
   // obsluguje zdarzenie hoover czy submit - w tym przykladzie submit
   // efekt jest taki ze wywolanie submit nie skutkuje przeladowaniem strony, ktorym to submit domyslnie skutkuje
   e.preventDefault()
   console.log("form_zapis_org")
   //Inny sposób na pobieranie danych z HTML
   //var wyswietl=document.getElementById("opis_organizacji").value
   //console.log("wyswietl:" +wyswietl )
   //var wyswietl2=$("#opis_organizacji").val()
   //console.log("wyswietl2: " +wyswietl2)

   var nazwa_org=$("#nazwa_organizacji").val()
   console.log("nazwa_org: "+ nazwa_org)
   var opis_org=$("#opis_organizacji").val()
   console.log("opis_org: " + opis_org)

   //jeszcze inny sposób tablicowy
   //var data = {};
   //data.nazwa = $("#nazwa_organizacji").val()
   //data.opis = $("#opis_organizacji").val()
   console.log("jestesmy w danych nowej organizacji")
   destinationURL = get_urls().url_home + get_urls().api_v1_organizacje
   console.log("current url:" + destinationURL)
   $.ajax({
      url      : destinationURL,
      type     : "POST",
      data     : {
          nazwa: nazwa_org,
          opis : opis_org,
          csrfmiddlewaretoken: csrftoken,
      },
      success: function(){
         console.log("nazwa org:"+ nazwa_org)
         console.log("opis org:" + opis_org)
         alert ('Save data');
      },
      failure: function(){
         alert ('Nie zostala dodana zmienna');
      }
   });
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
