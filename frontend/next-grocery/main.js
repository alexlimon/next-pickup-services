
document.getElementById('zipcode_text').addEventListener("keyup", async function(event) {
  if (event.keyCode === 13) {
      event.preventDefault();
      await queryStores();
  }
});


async function queryStores() {
  var zipcode = document.getElementById('zipcode_text').value;
  var pickupTable = document.getElementById('pickup-times-table');

  url = "https://next-pickup-services.azurewebsites.net/api/pickup/" + zipcode;

  fetch(url)
    .then(response => response.json())
    .catch(error => window.alert("Could not retrieve data! "))
    .then(function (data) {
      pickupTable.replaceChild(document.createElement('tbody'), pickupTable.getElementsByTagName('tbody')[0]);
      var pickupTableBody = pickupTable.getElementsByTagName('tbody')[0];

      var header_list = ['name', 'next_pickup_time', 'distance', 'location_link', 'store_hours'];
      if(data["store_list"].length <= 0){
        window.alert("No times available for that zipcode. Sorry!");
        return;
      }
      data["store_list"].forEach(element => {

        var currentRow = pickupTableBody.insertRow();
        col.appendChild(colText);

        //first element in the row with store brand and link to store
        var colText = document.createElement("a");
        colText.setAttribute("href", element["store_link"])
        var linkText = document.createTextNode(element["store_brand"]);
        colText.appendChild(linkText);

        for (var i = 0; i < header_list.length; i++) {
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