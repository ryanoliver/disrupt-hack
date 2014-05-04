chrome.tab.create({
  "title":"Version 1 Deploy",
  "onclick": sendPayload
});


function sendPayload(info, tab) {
  chrome.tabs.query({"active": true, "currentWindow": true}, function (tabs) {
    url = tab[0].url;
  });
}

