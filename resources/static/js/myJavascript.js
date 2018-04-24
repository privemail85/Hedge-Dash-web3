// Start: Related to Typeahead Plugin for stock search/////////////////////
 let stockSymbolArray = [];

// // Vanilla JavaScript Solution; Using XMLHttpRequest//////////////////
// defines the URL where we can find our JSON data from IEX API. Needs a link to their website. Read their terms below:
// Attribution
// If you redistribute our API data:
// Cite IEX using the following text and link: “Data provided for free by IEX.”
// Provide a link to https://iextrading.com/api-exhibit-a in your terms of service.
// Additionally, if you display our TOPS price data, cite “IEX Real-Time Price” near the price.

// This url is a made using a combination of:
// Endpoints
// All endpoints are prefixed with: https://api.iextrading.com/1.0
// AND
// Stocks: /ref-data/symbols
// This is the complete url:  "https://api.iextrading.com/1.0/ref-data/symbols";

const urlPrefix = "https://api.iextrading.com/1.0/";

// creates a new XMLHttpRequest object
const request = new XMLHttpRequest();

// builds the url for the API for stock names
const urlSymbols = urlPrefix + "ref-data/symbols";

// Specifies the request:
//Method (the request type GET or POST)
// url (the file location)
// async: true (asynchronous) or false (synchronous)
request.open('GET', urlSymbols, true);


request.onload = function() {
  if (request.status === 200) {
    const data = JSON.parse(request.responseText);
    let stockName;
    // goes through the jason data array
    for (let i = 0; i < data.length; i++) {

      stockName = data[i].symbol + " - " + data[i].name;

      //add stockName variable into the stockSymbolArray
      stockSymbolArray.push(stockName);

    }
  } else {
    // Reached the server, but it returned an error
  }
}

request.onerror = function() {
  console.error('An error occurred fetching the JSON from ' + urlSymbols);
};

// send(): Sends the request to the server (Used for GET requests)
request.send();
// End: Related to Typeahead Plugin for stock search//////////////


////// Start: getting the chosen stock price////////////////////

// to popup an alert box with the chosen stock
// This is just a function. It is not an object.
function newStockSelected() {
  let stockInputElement = document.getElementById("stockInput");
  let stockValue = stockInputElement.value;
  //alert(stockValue);

  let stockSplitArray = stockValue.split(" - ");
  //alert(stockSymbolArray);

  // Gives only the Symbol of the stock e.g. AAPL
  let stockSymbol = stockSplitArray[0];
  //alert(stockSymbol);

  // building the url to the API for price
  //Example of the url is: https://api.iextrading.com/1.0/stock/aapl/price
  const urlPrice = urlPrefix + "stock/" + stockSymbol + "/price";
  //alert(urlPrice);

  const request = new XMLHttpRequest();
  request.open('GET', urlPrice, true);

  request.onload = function() {
    if (request.status === 200) {
      
      const stockPrice = request.responseText;
      //alert(stockPrice);

      document.getElementById("realTimePrice").innerHTML = "$ " + stockPrice;

    } else {
      // Reached the server, but it returned an error
    }
  }

  request.onerror = function() {
    console.error('An error occurred fetching the data from ' + urlPrice);
  };

  // sends the remote request
  request.send();
}
////// END: getting the chosen stock price////////////////////
