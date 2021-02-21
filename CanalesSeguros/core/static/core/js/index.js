var sidebarLegajo = document.getElementById("legajo")
var sidebarLegajoPadre = document.getElementById("legajo-padre")

var navbarSearchClear = document.getElementById("cruz-search")

sidebarLegajoPadre.addEventListener("click",function(){
    sidebarLegajo.classList.toggle("fa-folder")
    sidebarLegajo.classList.toggle("fa-folder-open")
    
})

navbarSearchClear.addEventListener("click", function(){
    var navbarSearchInput = document.getElementById("input-search")
   
    navbarSearchInput.value=""
})

