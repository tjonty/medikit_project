function openForm() {
        document.getElementById("deletePopup").style.display="block";
  ***REMOVED***

function closeForm() {
       document.getElementById("deletePopup").style.display= "none";
}
      // When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    var modal = document.getElementById('deletePopup');
    if (event.target == modal) {
    closeForm();
***REMOVED***
}