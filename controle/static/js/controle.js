// Django CSRF //
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
// DJANGO RESCUE CSRF //

function delMed(cam,nome) {
	// console.log(nome);
	// console.log(cam);
	if(confirm('Deseja deletar este medicamento ? \n'+nome) == 1){
		window.location = cam;
	}
}

function delFon(cam,nome){
	if(confirm('Deseja deletar este fornecedor ? \n'+nome) == 1){
		window.location = cam;
	}
}
function delCli(cam,nome){
	if(confirm('Deseja deletar este cliente ? \n'+nome) == 1){
		window.location = cam;
	}
}
function delLot(cam,nome){
	if(confirm('Deseja deletar este lote ? \n'+nome) == 1){
		window.location = cam;
	}
}
function delMedE(cam,nome){
	if(confirm('Deseja deletar esta entrada ? \n'+nome) == 1){
		window.location = cam;
	}
}
function delMedS(cam,nome){
	if(confirm('Deseja deletar esta saida ? \n'+nome) == 1){
		window.location = cam;
	}
}

function pegaAltMed(id,nome,descricao){

	$("#idAlt").val(id);
	$("#nomeMedA").val(nome);
	$("#descMedA").val(descricao);

}

function pegaAltFornCli(id,nome,contato){

	$("#idAlt").val(id);
	$("#nomeAlt").val(nome)
	$("#contatoAlt").val(contato);

}

function pegaAltLot(id,fornecedor,numero,fabricacao,vencimento){
	$("#idAlt").val(id);
	$("#numeroAlt").val(numero);
	$("#fabAlt").val(fabricacao);
	$("#vencAlt").val(vencimento);
}

function pegaAltEnt(id,quant){
	$("#quantEnt").val(quant);
	$("#idAltEnt").val(id);

}
function pegaAltSai(quant){
	$("#quantSai").val(quant);
}


$("#formAlt").submit(function(event){

	var csrftoken = getCookie('csrftoken');
	// console.log(data);

	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    },
		url: 'alterar/',
		type: 'POST',
	});
	$.ajax({
		data: {'idAlt':$("#idAlt").val(),
			   'nome':$("#nomeMedA").val(),
			   'descricao':$("#descMedA").val()},
		success: function (response) {
			if(response == "Alterado"){
				$("#responseAlt").html("<div class='alert alert-success'>Alterado com sucesso</div>");
				alert('Alterado com sucesso !!');
				window.location = "";
			}else{
				$("#responseAlt").html(response);
			}
		}
	});

	return false;


});


$("#formAltFor").submit(function(event){

	var csrftoken = getCookie("csrftoken");

	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    },
		url: 'alterar/',
		type: 'POST'
	});
	$.ajax({
		data: {'idAlt':$("#idAlt").val(),
			   'nome':$("#nomeAlt").val(),
			   'contato':$("#contatoAlt").val()},
		success: function (response) {
			if(response == "Alterado"){
				$("#responseAlt").html("<div class='alert alert-success'>Alterado com sucesso</div>");
				alert('Alterado com sucesso !!');
				window.location = "";
			}else{
				$("#responseAlt").html(response);
			}
		}
	});
 	return false;
});

$("#formAltLot").submit(function(event){

	var csrftoken = getCookie("csrftoken");

	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    },
		url: 'alterar/',
		type: 'POST',
	});
	$.ajax({
		data: {'idAlt':$("#idAlt").val(),
			   'fornecedor':$("#fornAlt").val(),
			   'numero':$("#numeroAlt").val(),
			   'fabricacao':$("#fabAlt").val(),
			   'vencimento':$("#vencAlt").val()},
		success: function (response) {
			if(response == "Alterado"){
				$("#responseAlt").html("<div class='alert alert-success'>Alterado com sucesso</div>");
				alert('Alterado com sucesso !!');
				window.location = "";
			}else{
				$("#responseAlt").html(response);
			}
		}
	});

	return false;

})

// $("#entradaAlt").submit(function(event){
// 	var csrftoken = getCookie("csrftoken");
// 	console.log('a')
// 	$.ajaxSetup({
// 		beforeSend: function(xhr, settings) {
// 	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
// 	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
// 	        }
// 	    },
// 		url: 'alterar/',
// 		type: 'POST',
// 	});
// 	$.ajax({
// 		data: {'usuario':$("#idAltEnt").val(),
// 		   'lote':$("#loteAltEnt").val(),
// 		   'quantidade':$("#quantEnt").val(),
// 		   'medicamento':$("#idMedEnt").val()},
// 		success: function (response) {
// 			if(response == "Alterado"){
// 				$("#responseAlt").html("<div class='alert alert-success'>Alterado com sucesso</div>");
// 				alert('Alterado com sucesso !!');
// 				window.location = "";
// 			}else{
// 				$("#responseAlt").html(response);
// 			}
// 		}
// 	});

// 	return false;
// });

// $("#saidaAlt").submit(function(event){

// });

var cont = 1;
var contS = 1;
$("#adicionarMedicamento").on('click',function(){

	$('<strong>Medicamento</strong>'+
					'<select name="medicamento" class="form-control" required>'+
						$("#medicamentoEnt").html()+
					'</select>'+
					'<strong>Quantidade</strong>'+
					'<input type="number"  maxlength="5" name="quantidade" class="form-control" required><br>').insertAfter("#entradaadd br:last-child");
	cont++;
});

$("#adicionarMedicamentoS").on('click',function(){

	$('<strong>Medicamento</strong>'+
					'<select name="medicamento" class="form-control" required>'+
						$("#medicamentoEnt").html()+
					'</select>'+
					'<strong>Quantidade</strong>'+
					'<input type="number" maxlength="5" name="quantidade" class="form-control" required><br/>').insertAfter("#saidaadd br:last-child");

	contS++;
});


$("#deletarMedicamento").on('click',function(){

	if(cont != 1){
		var child = $("#entradaadd select").length;
		$("#entradaadd select")[child-1].remove();
		$("#entradaadd input")[child-1].remove();
		$("#entradaadd br")[child-1].remove();
		$("#entradaadd strong")[$("#entradaadd strong").length-1].remove();
		$("#entradaadd strong")[$("#entradaadd strong").length-1].remove();
		cont--;
	}

});

$("#deletarMedicamentoS").on('click',function(){

	if(contS != 1){

		var child = $("#saidaadd select").length;
		$("#saidaadd select")[child-1].remove();
		$("#saidaadd input")[child-1].remove();
		$("#saidaadd br")[child-1].remove();
		$("#saidaadd strong")[$("#saidaadd strong").length-1].remove();
		$("#saidaadd strong")[$("#saidaadd strong").length-1].remove();
		contS--;
	}

});
