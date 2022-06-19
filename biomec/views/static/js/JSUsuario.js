// JavaScript Document

$(document).ready(function(){
	fn_buscar();
	$("#grilla tbody tr").mouseover(function(){
		$(this).addClass("over");
	}).mouseout(function(){
		$(this).removeClass("over");
	});
});

function fn_cerrar() {
    $.unblockUI({
        onUnblock: function () {
        }
    });
};

function fn_mostrar_frm_agregar(){
	//$("#div_oculto").load("ajax_form_agregar.php", function(){
        
        //alert($.fn.jquery);
        try{
        $.blockUI({
            message: $('#div_agregar'),
            css: {
                            top: '5%',
                            left: '20%',
                            width: '65%',
                            bottom: '5%'                             
            }
        }); 
        }catch(err){
        alert(err);
        }
};

function fn_mostrar_frm_modificar(DatoTipo,id,name,pass){
	//$("#div_oculto").load("ajax_form_modificar.php", {ide_per: ide_per}, function(){
		$('#id_Tipo').val(DatoTipo);
                $('#id_modif').val(id);
                $('#name_modif').val(name);
                $('#pass_modif').val(pass);
                //alert(id_metodo+name_metodo);
                $.blockUI({
			message: $('#div_modif'),
			css:{
                            top: '5%',
                            left: '30%',
                            width: '50%',
                            bottom: '25%'   
			}
		}); 
	//});
};

function fn_paginar(var_div, url){
	var div = $("#" + var_div);
	$(div).load(url);
	/*
	div.fadeOut("fast", function(){
		$(div).load(url, function(){
			$(div).fadeIn("fast");
		});
	});
	*/
}

function fn_eliminar(id_metodo){
	var respuesta = confirm("Desea eliminar esta Sucursal?");
	if (respuesta){
            $.blockUI({
                message: '<h3>Eliminado..</h3><br><img align="center" id="imgAjaxModif" src="../images/ajax-load.gif"><br>'
            });
            $.ajax({
                url: 'gestionar_sucursal.php',
                data: 'id_sucursal=' + id_metodo,
                type: 'post',
                success: function(data){
                    if(data!=""){
                        alert(data);
                    }else{
                        alert("Se elimino correctamente"+data);
                        fn_cerrar();
                        fn_buscar();
                    }
                    $.unblockUI();
                }
            });
	}
}

function fn_buscar(){
    var str = $("#frm_buscar").serialize();
    $("#btnBuscar").hide();
    $("#imgAjax").show();

    $.ajax({
            url: 'ListaUsuario.php',
            type: 'get',
            data: str,
            success: function(data){
                $("#div_listar").html(data);
                $("#btnBuscar").show();
                $("#imgAjax").hide();
            }
    });
}