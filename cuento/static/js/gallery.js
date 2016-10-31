function showCap(list, index){
	$.each(list, function(idx, valIs) {
		if((valIs).id == index){
			$(valIs).css("display", "block");
		} else {
			$(valIs).css("display", "none");
		}
    });
}

function btnPick(lista, direccion, index){
	if (direccion == "left"){
		if(index !=1){
			index -= 1;
		}
	} else {
		if (index != lista.length){
			index +=1;
		} 
	}
	showCap(lista, index);
	return index;
}

$(document).ready(function(){
	var index = 1;
	var listCuentos = $(".capitulo").get();
			
	showCap(listCuentos, index);

	$("#left").click(function(){
		index = btnPick(listCuentos, "left", index);
	});
	$("#right").on("click", function(){
		index = btnPick(listCuentos, "right", index);
	});
})