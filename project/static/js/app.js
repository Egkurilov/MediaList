/*var exampleModal = document.getElementById('exampleModal')
exampleModal.addEventListener('show.bs.modal', function (event) {
  // Button that triggered the modal
  var button = event.relatedTarget
  // Extract info from data-bs-* attributes
  var recipient = button.getAttribute('data-bs-whatever')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  var modalTitle = exampleModal.querySelector('.modal-title')
  var modalBodyInput = exampleModal.querySelector('.modal-body input')

  modalTitle.textContent = 'New message to ' + recipient
  modalBodyInput.value = recipient
})*/

jQuery(document).ready(function($) {

    var timeout = null;

    $("input#searchInput").keyup(function(e){

        var $this = $(this);
        clearTimeout(timeout);

        timeout = setTimeout(function() {

            $.post(`/ajax/search?q=${$this.val()}`, function(data){
                console.log(data);
            }, 'json');

        }, 500);
    });

});