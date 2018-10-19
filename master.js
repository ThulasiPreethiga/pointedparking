function validate(id) {
    var x = document.getElementById('b1').value;
    if (x == "Book Now") {

        document.getElementById('b1').innerHTML="Booked";
        document.getElementById('b1').value="Booked";
        document.getElementById('lot1').style.backgroundColor = "red";
        document.getElementById('b2').style.display="inline";
        document.getElementById('b3').style.display="inline";
        document.getElementById("p1").innerHTML="Booked";
      // obj = {"status":"Booked" };
      // dbParam = JSON.stringify(obj);

//       xmlhttp = new XMLHttpRequest();
//       xmlhttp.onreadystatechange = function() {
//           if (this.readyState == 4 && this.status == 200) {
//               // document.getElementById("demo").innerHTML = this.responseText;
//           }
//       };
//       xmlhttp.open("GET", "demo.php?x=" + dbParam, true);
//       xmlhttp.send();
// var dataString = JSON.stringify(obj);
// console.log(dataString);

$.ajax({
   url: 'demo.php',
   data: {"booked": true,"id":id},
   type: 'POST',
   success: function(response) {
      alert(response);
      console.log(response);
   }
});

    }else if (x == 'Booked') {
      document.getElementById('b1').innerHTML="Book Now";
      document.getElementById('b1').value="Book Now";
      document.getElementById('b2').style.display="none";
      document.getElementById('b3').style.display="none";
      document.getElementById("p1").innerHTML="Free";
    }


}

function park(id) {
  document.getElementById("p1").innerHTML="Parked"
  $.ajax({
     url: 'demo.php',
     data: {"park": true,"id":id},
     type: 'POST',
     success: function(response) {
        alert(response);
         console.log(response);
     }
  });
}

function makeFree(id) {
  // document.getElementById("p1").innerHTML="Free";
  // document.getElementById('b1').innerHTML="Book Now";
  // document.getElementById('b1').value="Book Now";
  // document.getElementById('lot1').style.backgroundColor = "#1AF312";
  // document.getElementById('b2').style.visibility="hidden";
  // document.getElementById('b3').style.visibility="hidden";
  location.reload();

  $.ajax({
     url: 'demo.php',
     data: {"remove": true,"id":id},
     type: 'POST',
     success: function(response) {
        alert(response);
        console.log(response);
     }
  });
}
