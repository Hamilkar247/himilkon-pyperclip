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

//uzupelnianie liste organizacji
$( document ).ready(function() {

   console.log("funkcja uzupelnianie organization_table")
   $('#organization_table').DataTable( {
        ajax: {
         url:  revers_urls.api_v1_organizacje,
         type: "GET",
         dataSrc: "",
        },

        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'copyHtml5',
                exportOptions: {
                    columns: [ 0, ':visible' ]
                }
            },
            {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'pdfHtml5',
                exportOptions: {
                    columns: [ 0, 1, 2 ]
                }
            },
            {
                extend: 'colvis',
                columns: ':not(.noVis)'
            }
        ],
        columns: [
            { data: 'id' },
            { data: 'nazwa' },
            { data: 'opis' },
            { data: 'id',
              render: function (data, type, full, meta) {
                numer = data
                return '<a href="'  + revers_urls.front_organizacje  + numer + '" class="btn btn-w-m btn-success"> Edytuj </a>';
              }
            },
        ]
    })
})
