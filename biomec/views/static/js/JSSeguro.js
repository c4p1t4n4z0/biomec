$(document).ready(function () {
    fn_buscar();
    $("#grilla tbody tr").mouseover(function () {
        $(this).addClass("over");
    }).mouseout(function () {
        $(this).removeClass("over");
    });
    $("#criterio_usu_per").keyup(function () {
        fn_buscar();
    });

});

function fn_cerrar() {
    $.unblockUI({
        onUnblock: function () {
        }
    });
};

function fn_mostrar_frm_agregar() {
    $.blockUI({message: $('#div_oculto'), css: {top: '20%'}});
};

function fn_mostrar_frm_modificar(idSeguro, name_seguro) {
    $('#seguro_name_modif').val(name_seguro);
    $('#id_seguro_modif').val(idSeguro);
    $.blockUI({message: $('#div_modif'), css: {top: '20%'}});
};

function fn_paginar(var_div, url) {
    var div = $("#" + var_div);
    $(div).load(url);
    /*	div.fadeOut("fast", function(){		$(div).load(url, function(){			$(div).fadeIn("fast");		});	});	*/
}

function fn_buscar() {
    var str = $("#frm_buscar").serialize();
    $("#btnBuscar").hide();
    $("#imgAjax").show();
    $.ajax({
        url: 'ListaSeguro.php', type: 'get', data: str, success: function (data) {
            $("#div_listar").html(data);
            $("#btnBuscar").show();
            $("#imgAjax").hide();
        }
    });
}

function redirect_by_post(purl, pparameters, in_new_tab) {
    pparameters = (typeof pparameters == 'undefined') ? {} : pparameters;
    in_new_tab = (typeof in_new_tab == 'undefined') ? true : in_new_tab;
    var form = document.createElement("form");
    $(form).attr("id", "reg-form").attr("name", "reg-form").attr("action", purl).attr("method", "post").attr("enctype", "multipart/form-data");
    if (in_new_tab) {
        $(form).attr("target", "_blank");
    }
    $.each(pparameters, function (key) {
        $(form).append('<input type="text" name="' + key + '" value="' + this + '" />');
    });
    document.body.appendChild(form);
    form.submit();
    document.body.removeChild(form);
    return false;
}

function fn_agregar() {
    var str = $("#frm_agregar_seguro").serialize();
    $.ajax({
        url: 'gestionar_seguro.php', data: str + '&proc=agregar', type: 'get', success: function (data) {
            var idS = $.trim(data);
            if (!$.isNumeric(idS)) {
                alert(data);
            } else {
                alert("se registro correctamente \n !!! Ahora se procedera a registrar el precio de cada uno de los Analisis que dispone el Laboratorio !!!");
                fn_cerrar();
                fn_buscar();
                redirect_by_post('SeguroAnalisis.php', {idS: idS}, false);
            }
        }
    });
}

function fn_eliminar(id_seguro) {
    var respuesta = confirm("Desea eliminar este Seguro?");
    if (respuesta) {
        $.blockUI({message: '<h3>Eliminando...</h3><br><img align="center" id="imgAjaxModif" src="../images/ajax-load.gif"><br>'});
        $.ajax({
            url: 'gestionar_seguro.php', data: 'id_seguro=' + id_seguro, type: 'post', success: function (data) {
                if (data != "") {
                    alert(data);
                } else {
                    alert("Se Elimino Correctamente" + data);
                    fn_cerrar();
                    fn_buscar();
                }
            }
        });
    }
}

function fn_SeguroAnalisis(id_seguro, name_seguro) {
    var respuesta = confirm("Desea Modificar la Lista de Precios del Seguro: \n " + name_seguro);
    if (respuesta) {
        $.blockUI({message: '<h3>Redirreccionando...</h3><br><img align="center" id="imgAjaxModif" src="../images/ajax-load.gif"><br>'});
        $.ajax({
            data: 'id_seguro=' + id_seguro, type: 'post', success: function (data) {
                redirect_by_post('SeguroAnalisis.php', {idS: id_seguro}, false);
            }
        });
    }
}

function fn_modificar() {
    var str = $("#frm_modif_seguro").serialize();
    $.ajax({
        url: 'gestionar_seguro.php', data: str + '&proc=modif', type: 'get', success: function (data) {
            if ($.trim(data) != "correcto") {
                alert(data + '---');
            } else {
                alert("se actualizo correctamente");
                fn_cerrar();
                fn_buscar();
            }
        }
    });
}