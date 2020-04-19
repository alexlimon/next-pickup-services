var zipcode = document.getElementById('zipcode_text');
var pickupTable = document.getElementById('pickup-times-table');


zipcode.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
      event.preventDefault();
      queryStores();
  }
});



async function queryStores() {
  
  url = "https://next-pickup-services.azurewebsites.net/api/pickup/" + zipcode.value;

  fetch(url)
    .then(response => response.json())
    .catch(error => window.alert("Could not retrieve data! "))
    .then(function (data) {
      pickupTable.replaceChild(document.createElement('tbody'), pickupTable.getElementsByTagName('tbody')[0]);
      var pickupTableBody = pickupTable.getElementsByTagName('tbody')[0];
      var store_brand = data["name"];

      var header_list = ['store_brand', 'name', 'next_pickup_time', 'distance', 'location_link', 'store_hours'];
      if(data["store_list"].length <= 0){
        window.alert("No times available for that zipcode. Sorry!");
        return;
      }
      data["store_list"].forEach(element => {

        var currentRow = pickupTableBody.insertRow();
        var col = currentRow.insertCell(0);
        var colText = document.createTextNode(store_brand);
        col.appendChild(colText);

        for (var i = 1; i < 6; i++) {
          var col = currentRow.insertCell(i);
          if(i == 4){
            var colText = document.createElement("a");
            colText.setAttribute("href", element[header_list[i]])
            var linkText = document.createTextNode("Location Link");
            colText.appendChild(linkText);
          }
          else{
            var colText = document.createTextNode(element[header_list[i]]);
          }
          col.appendChild(colText);
        }
      });
     }).
     catch(function(error){
       window.alert("Invalid zipcode or store does not exist within 10 mile radius.");
     })

}