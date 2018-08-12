"use strict";

$(document).ready(function(){

    $('#load-customer').on('input propertychange',function(){
        $.ajax({
            url: "/admin/customer/load-customer",
            data: {
                id: $('#load-customer').val()
            },
            type: "POST",
            beforeSend: function() {
                
            },
            error: function(data) {
                
            },
            success: function(data) {
                $('#show-load-customer').html(data);
                $('#show-load-customer').show();
               
                $('#show-load-customer li').on('click',function(){
                    $('#load-customer').val($(this).data('username'));
                    $('#p_node_append').val($(this).data('id'));
                    $('#show-load-customer').hide();
                })
            }
        });
    })

    $('#load-customer-position').on('input propertychange',function(){
        $.ajax({
            url: "/admin/customer/load-customer-position",
            data: {
                id: $('#load-customer-position').val()
            },
            type: "POST",
            beforeSend: function() {
                
            },
            error: function(data) {
                
            },
            success: function(data) {
                $('#show-load-customer-position').html(data);
                $('#show-load-customer-position').show();
               
                $('#show-load-customer-position li').on('click',function(){
                    $('#load-customer-position').val($(this).data('username'));
                    $('#p_binary_append').val($(this).data('id'));
                    $('#show-load-customer-position').hide();

                    if (parseInt($(this).data('position')) == 0)
                    {
                        $('#position').html('<option value="1">Bên trái</option><option value="2">Bên phải</option>')
                    }

                    if (parseInt($(this).data('position')) == 1)
                    {
                        $('#position').html('<option value="1">Bên trái</option>')
                    }
                    if (parseInt($(this).data('position')) == 2)
                    {
                        $('#position').html('<option value="2">Bên phải</option>')
                    }

                })
            }
        });
    })


    $('#verify').click(function(){
            if($(this).is(':checked')){
                document.getElementById("submitRegister").disabled = false;
            } else {
                document.getElementById("submitRegister").disabled = true; 
            }
        });


    $('.active_account_id').on('click',function(){
        //alert($(this).data('id'));
        $('#modalActiveCode #username_account').html($(this).data('username'));
        $('#modalActiveCode #customer_id').val($(this).data('id'));
        
        $('#modalActiveCode').modal('show');
    })

    $('#modalActiveCode #btnActiveCode').click(function(evt) {
        $.ajax({
            url: "/account/activecode",
            data: {
                code: $('#modalActiveCode #code').val(),
                customer_id: $('#modalActiveCode #customer_id').val()
            },
            type: "POST",
            beforeSend: function() {
                $('.btnConfirm').button('loading');
            },
            error: function(data) {
                $('.btnConfirm').button('reset');
            },
            success: function(data) {
                $('.btnConfirm').button('reset');
                var data = $.parseJSON(data);
                data.status == 'error' ? (
                    showNotification('top', 'right', data.message, 'danger')
                ) : (
                    showNotification('top', 'right', data.message, 'success')
                    
                   //setTimeout(function() {location.reload(true)}, 3)
                )
            }
        });

    });
});

function showNotification(from, align, msg, type) {
        /* type = ['','info','success','warning','danger','rose','primary'];*/
        var color = Math.floor((Math.random() * 6) + 1);
        $.notify({
            icon: "notifications",
            message: msg
        }, {
            type: type,
            timer: 3000,
            placement: {
                from: from,
                align: align
            }
        });
    }
$('#submitLogin').click(function(){
    $('form#frmLogin').submit();
    $('#submitLogin').hide();
})
$('#submitRegister').click(function(){
    $('form#frmRegister').submit();
    $('#submitRegister').hide();
})

$('#submitReset').click(function(){
    $('form#frmReset').submit();
    $('#submitReset').hide();
})