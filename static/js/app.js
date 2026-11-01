// Register service worker
if ("serviceWorker" in navigator) {
  window.addEventListener("load", function () {
    navigator.serviceWorker
      .register("static/js/serviceworker.js")
      .then((res) => console.log("service worker registered"))
      .catch((err) => console.log("service worker not registered", err));
  });
}

// Online/Offline detection
const offlineBanner = document.getElementById("offline-banner");

function updateOnlineStatus() {
  if (navigator.onLine) {
    // User is online
    offlineBanner.style.display = "none";
    console.log("App is online");
  } else {
    // User is offline
    offlineBanner.style.display = "block";
    console.log("App is offline");
  }
}

// Check status when page loads
window.addEventListener("load", updateOnlineStatus);
// Update the banner when the browser goes offline
window.addEventListener("offline", updateOnlineStatus);
// Listen for online event
window.addEventListener("online", function () {
  offlineBanner.style.display = "none";

  // Show temporary "back online" message
  const tempBanner = document.createElement("div");
  tempBanner.className = "online-banner";
  tempBanner.innerHTML = "<p>✅ You're back online!</p>";
  document.body.prepend(tempBanner);

  // Remove message after 3 seconds
  setTimeout(() => {
    tempBanner.remove();
  }, 3000);

  console.log("Connection restored");
});

// Add this after the event listeners
document
  .getElementById("retry-connection")
  .addEventListener("click", function () {
    // Force a check by trying to fetch a small resource
    fetch("/", { method: "HEAD", cache: "no-store" })
      .then(() => {
        console.log("Connection test successful");
        updateOnlineStatus();
      })
      .catch(() => {
        console.log("Still offline");
        alert("Still no connection. Please check your network settings.");
      });
  });
