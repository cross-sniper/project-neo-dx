(function(){
	try{
		player = {
			local:"/void",
			inv:[],
			//add more things here
		}
	    console.log("project neo runtime v0.1");

	    // Get all elements with the name "div"
	    var divElements = document.getElementsByTagName("div");

	    // Hide all elements with the name "div"
	    for (var i = 0; i < divElements.length; i++) {
	        divElements[i].style.display = "none";
	    }
		goto(player.local)

	    // Show the element with the id "start"

	}catch(e){
		alert(e)
	}
})();

function goto(place_id)
{
	try {
		document.getElementById(player.local).style.display = "none";
		var element = document.getElementById(place_id);
		element.innerHTML = processContent(element.innerHTML)
		element.style.display = '';
		player.place = place_id
	} catch(e) {
		// statements
		alert(e);
		goto("/void")
	}
}



function processContent(content) {
    // Regular expression to match custom syntax

    // Replace custom syntax with HTML button elements
    content = content.replace(/\[\[(.*)\|(.*)\]\]/, '<button onclick="goto(\'$2\')">$1</button>');

    return content;
}

