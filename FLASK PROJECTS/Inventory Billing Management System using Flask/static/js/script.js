// Custom Loader Element Node
var loader = document.createElement('div')
loader.setAttribute('id', 'pre-loader');
loader.innerHTML = "<div class='lds-hourglass'></div>";

// Loader Start Function
window.start_loader = function() {
    if (!document.getElementById('pre-loader') || (!!document.getElementById('pre-loader') && document.getElementById('pre-loader').length <= 0))
        document.querySelector('body').appendChild(loader)
}

// Loader Stop Function
window.end_loader = function() {
    if (!!document.getElementById('pre-loader')) {
        setTimeout(() => {
            document.getElementById('pre-loader').remove()
        }, 500)
    }
}

var prod_ajax, products, listed, total = 0,
    change = 0;

function product_actions(_this, data) {
    var form = $("#add-form")
    _this.click(function() {
        form.find('input[name="name"]').val(data.name)
        form.find('input[name="price"]').val(data.price)
        $('#pname').text(data.name)
        $('#pprice').text(parseFloat(data.price).toLocaleString('en-US'))
        $('#pid').text(data.item_id)
        $('#pdesc').text(data.item_description)
        $('#find-product').val('').trigger('input')
    })

}

function update_total() {
    $('#total-amount').text(parseFloat(total).toLocaleString('en-US', { style: 'decimal', maximumFractionDigits: 2, minimumFractionDigits: 2 }))
    $('#checkout-amount').val(parseFloat(total).toLocaleString('en-US', { style: 'decimal', maximumFractionDigits: 2, minimumFractionDigits: 2 }))
}

function load_products() {
    if (prod_ajax) {
        prod_ajax.abort()
    }
    find_prod_ajax = $.ajax({
        url: 'static/js/product_json.json',
        dataType: 'json',
        error: err => {
            alert('An error occurred.')
            console.error(err)
        },
        success: function(resp) {
            console.log(`resp:${resp[0].name}`)
            products = resp
            $('#product-result').html('')
            Object.keys(resp).map(k => {
                var item = $($('noscript#prod-item-clone').html()).clone()
                item.find('.prod_name').text(resp[k].name)
                item.find('.prod_price').text(parseFloat(resp[k].price).toLocaleString('en-US'))
                item.find('.prod_price').attr('data-id', resp[k].price)
                $('#product-result').append(item)
                product_actions(item, resp[k])
            })
        }
    })
}

function check_items() {
    if ($("#item-list tbody").is(':empty') == true) {
        $('#noItem').removeClass('d-none')
    } else {
        if ($('#noItem').hasClass('d-none') == false)
            $('#noItem').addClass('d-none');
    }
}

function item_actions(_this, key) {
    _this.find('.rem-item').click(function() {
        if (!!listed[key]) {
            _this.remove()
            delete listed[key];
            listed = Object.keys(listed).map(k => { return listed[k] != null ? listed[k] : false })
            localStorage.setItem('listed', JSON.stringify(listed))
        }
        check_items()
        load_list()
    })
    _this.find('.qty').on('change input', function() {
        if (!!listed[key]) {
            listed[key].qty = $(this).val()
            localStorage.setItem('listed', JSON.stringify(listed))
        }
        load_list()
    })
}

function load_list() {
    listed = !!localStorage.getItem('listed') ? $.parseJSON(localStorage.getItem('listed')) : [];
    total = 0;
    $('#item-list tbody').html('')
    if (Object.keys(listed).length > 0) {
        Object.keys(listed).map((k) => {
            var item = $($('noscript#item-tr-clone').html()).clone()
            item.find('.qty').val(parseFloat(listed[k].qty))
            item.find('.item-name').text(listed[k].product)
            item.find('.item-price').text(parseFloat(listed[k].price).toLocaleString('en-US'))
            item.find('.item-total').text(parseFloat(parseFloat(listed[k].price) * parseFloat(listed[k].qty)).toLocaleString('en-US'))
            total += parseFloat(listed[k].price) * parseFloat(listed[k].qty);
            $('#item-list tbody').append(item)
            item_actions(item, k)
            update_total()
        })
    }
    check_items()
}
$(function() {
    check_items()
    load_list()
    var load_prod = new Promise((resolve) => {
        load_products()
        resolve()
    })
    console.log(load_prod)
    load_prod.then(() => {
        end_loader()
    })
    $('#find-product').on('input', function() {
        var search = $(this).val().toLowerCase()
        if (search == '') {
            if (!$('#product-result').hasClass('d-none'))
                $('#product-result').addClass('d-none');
            return false;
        }
        $('#product-result').removeClass('d-none');
        $('#product-result .prod-item').each(function() {
            var name = $(this).find('.prod_name').text().toLowerCase()
            if (name.includes(search) === true) {
                $(this).toggle(true)
            } else {
                $(this).toggle(false)
            }

        })

    })
    $('#add-form').submit(function(e) {
        e.preventDefault()
        start_loader()
        var _this = $(this)
        var product = _this.find('[name="name"]').val()
        var price = _this.find('[name="price"]').val()
        var qty = _this.find('[name="qty"]').val()
        listed[listed.length] = { product: product, price: price, qty: qty, item_id: document.getElementById("pid").innerHTML}
        localStorage.setItem('listed', JSON.stringify(listed))
        _this[0].reset()
        _this.find('[name="name"]').val('')
        _this.find('[name="price"]').val('')
        $('#pname').text('')
        $('#pprice').text('')
        $('#pdesc').text('')
        // $('#pprice').text('')
        load_list()
        end_loader()
    })

    $('#checkout').click(function() {
        if(listed == "" || listed == "[]" || listed == []){
            alert("Add atleast 1 item in the list")
           
        } else{
            $('#checkoutModal').modal('show')
            $('#checkoutModal').on('shown.bs.modal', function() {
                $('#checkout-tendered').focus()
                $('#checkout-tendered').on('change input', function() {
                    var pay = $(this).val()
                    change = -parseFloat(pay) + parseFloat(total)
                    $('#checkout-change').val(parseFloat(change).toLocaleString('en-US'))
                })
            })
        }
    })
    $('#checkout-form').submit(function(e) {
        e.preventDefault()
        start_loader()
        if (change >= 0) {
            $.ajax({
                url: 'static/js/receipt_format.html',
                error: err => {
                    console.error(err)
                    alert('An error occurred.')
                    end_loader()
                },
                success: function(resp) {
                    var el = $('<div>')
                    el.html(resp)
                    el.find('#r-total').text(parseFloat(total).toLocaleString('en-US', { style: 'decimal', maximumFractionDigits: 2, minimumFractionDigits: 2 }))
                    el.find('#r-tendered').text(parseFloat(parseFloat(total) + parseFloat(change)).toLocaleString('en-US', { style: 'decimal', maximumFractionDigits: 2, minimumFractionDigits: 2 }))
                    el.find('#r-change').text(parseFloat(change).toLocaleString('en-US', { style: 'decimal', maximumFractionDigits: 2, minimumFractionDigits: 2 }))
                    Object.keys(listed).map((k) => {
                        el.find('#product-list').append('<div class="col-1 text-center">' + (parseFloat(listed[k].qty).toLocaleString('en-US')) + '</div>')
                        el.find('#product-list').append('<div class="col-8 text-start lh-1">' + (listed[k].product) + '<div><small>x ' + (parseFloat(listed[k].price).toLocaleString('en-US', { style: 'decimal', maximumFractionDigits: 2, minimumFractionDigits: 2 })) + '</small></div></div>')
                        el.find('#product-list').append('<div class="col-3 text-end">' + (parseFloat(listed[k].qty * listed[k].price).toLocaleString('en-US', { style: 'decimal', maximumFractionDigits: 2, minimumFractionDigits: 2 })) + '</div>')
                    })


                    var nw = window.open('', '_blank', 'width=1000,height=900')
                    console.log(el.html())
                    nw.document.write(el.html())
                    nw.document.close()
                    setTimeout(() => {
                        nw.print()
                        setTimeout(() => {
                            nw.close()
                            end_loader()
                            $('.modal').modal('hide')
                            localStorage.setItem('listed', '[]')
                            location.reload()
                        }, 300)
                    }, 500)
                }
            })
        } else {
            alert("Tendered Amount less than payable amount!")
        }
    })
})