const recentsBox = document.getElementById("more-recent")
const imageOffert = document.getElementById("image-offert")

let image = "";
function test(){
    $.ajax({
      type: "GET",
      url: "/load",
      success: function(response) {
        const data = response.lasts;
        data.forEach(el => {
          image = data[0].image;
          recentsBox.innerHTML += `
           <div class="col-md-4 product-men mt-5">

									<div class="men-pro-item simpleCart_shelfItem">

										<div class="men-thumb-item text-center">
											<img class="image-fluid" src="${el.image}" alt="">
											<div class="men-cart-pro">
												<div class="inner-men-cart-pro">
													<a href="details/${el.id}" class="link-product-add-cart">Vista Rápida</a>
												</div>
											</div>
											    ${el.offert ? '<span class="product-new-top">Oferta</span>' : ''} 
											
										</div>
										<div class="item-info-product text-center border-top mt-4">
											<h4 class="pt-1">
												<a href="details/${el.id}">${el.name}</a>
											</h4>
											<div class="info-product-price my-2">
											  
												  ${el.offert ? '<span class="item_price">$45000</span> <del>$6799</del>' : '<span class="item_price">$6789</span>'}
												 
												 
											</div>
											<div class="snipcart-details top_brand_home_details item_add single-item hvr-outline-out">
												<form action="#" method="post">
												
													<fieldset>
														<input type="hidden" name="cmd" value="_cart" />
														<input type="hidden" name="add" value="1" />
														<input type="hidden" name="business" value=" " />
														<input type="hidden" name="item_name" value="${el.name}" />
														<input type="hidden" name="amount" value="${el.price}" />
														<input type="hidden" name="discount_amount" value="1.00" />
														<input type="hidden" name="currency_code" value="COP" />
														<input type="hidden" name="return" value=" " />
														<input type="hidden" name="cancel_return" value=" " />
														<input type="submit" name="submit" value="Añadir al carrito" class="button btn" />
													</fieldset>
												</form>
											</div>
										</div>
									</div>
								</div>
          `
        //  imageOffert.src = image
        })
      },
      error: function(error) {
        alert("error generado")
      }
    }); 
}

test()
