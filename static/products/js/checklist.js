const outputBox = document.getElementById("checkout-box");
const itemCountsEl = document.querySelector(".items-count");
function test(){
    $.ajax({
      type: "GET",
      url: "/checkout",
      success: function(response) {
        const data = response.list;
        data.forEach(el => {
          
          outputBox.innerHTML += `
           <tr class="rem1">
								<td class="invert">${el.id}</td>
								<td class="invert-image">
									<a href="single.html">
										<img src="${el.image}" alt=" " class="img-responsive">
									</a>
								</td>
								<td class="invert">
									<div class="quantity">
										<div class="quantity-select">
											<div class="entry value-minus">&nbsp;</div>
											<div class="entry value">
												<span>${el.quantity}</span>
											</div>
											<div class="entry value-plus active">&nbsp;</div>
										</div>
									</div>
								</td>
								<td class="invert">${el.name}</td>
								<td class="invert">$${el.price}</td>
								<td class="invert">
									<div class="rem">
										<div class="close1"></div>
									</div>
								</td>
							</tr>
          `
          itemCountsEl.textContent = el.id;
        })
      },
      error: function(error) {
        alert(error)
      }
    }); 
}

test()



