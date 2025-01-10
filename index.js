function toggleDroplist() {
  const droplist = document.querySelector("dropdown-content");
  const mapDiv = document.querySelector("mapdiv");

  if (droplist.style.display === "block") {
    droplist.style.display = "none";
    mapDiv.style.visibility = "visible";
  } else {
    droplist.style.display = "block";
    mapDiv.style.visibility = "hidden";
  }
}

document.querySelector("menu-item").addEventListener("click", toggleDroplist);