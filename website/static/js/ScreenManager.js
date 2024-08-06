console.log(`[INFO]: Loaded page to screen ${current_screen}`)

// ScreenElement, ScreenID 

main_screen = [document.querySelector("#main-screen"), 1]
profile_screen = [document.querySelector("#profile-screen"), 2]
// document_upload_screen = [document.querySelector("#document-upload-screen"), 5]
create_screen = [document.querySelector("#create-screen"), 3]
// order_screen = [document.querySelector("#order-screen"), 94]
merchant_screen = [document.querySelector("#merchant-screen"), 23]

// Trigger's
main_trigger = document.querySelector("#home-trigger")
profile_trigger = document.querySelector("#profile-trigger")
create_trigger = document.querySelector("#create-trigger")
merchant_trigger = document.querySelector("#merchant-trigger")

window.addEventListener('load', ()=>{
	// window.location.href = `/dashboard/${current_screen}`
	switch (current_screen) {
	
		case 2:
			main_screen[0].style.display = 'none'
			// settings_screen[0].style.display = "none"
			create_screen[0].style.display = 'none'
			// order_screen[0].style.display = 'none'
			merchant_screen[0].style.display = 'none'
			profile_screen[0].style.display = 'block'
			current_screen = 2
			break;

		case 3:
			main_screen[0].style.display = 'none'
			// document_upload_screen[0].style.display = "none"
			create_screen[0].style.display = 'block'
			// order_screen[0].style.display = 'none'
			merchant_screen[0].style.display = 'none'
			profile_screen[0].style.display = 'none'
			current_screen = 3
			break;

		case 5:
			main_screen[0].style.display = 'none'
			// document_upload_screen[0].style.display = "block"
			create_screen[0].style.display = 'none'
			// order_screen[0].style.display = 'none'
			merchant_screen[0].style.display = 'none'
			profile_screen[0].style.display = 'none'
			current_screen = 5
			break;

		case 94:
			main_screen[0].style.display = 'none'
			// document_upload_screen[0].style.display = "none"
			create_screen[0].style.display = 'none'
			// order_screen[0].style.display = 'block'
			merchant_screen[0].style.display = 'none'
			profile_screen[0].style.display = 'none'
			current_screen = 94
			break;

		case 23:
			main_screen[0].style.display = 'none'
			// document_upload_screen[0].style.display = "none"
			create_screen[0].style.display = 'none'
			// order_screen[0].style.display = 'none'
			merchant_screen[0].style.display = 'block'
			profile_screen[0].style.display = 'none'
			current_screen = 23
			break;


		default:
			main_screen[0].style.display = 'block'
			// document_upload_screen[0].style.display = "none"
			create_screen[0].style.display = 'none'
			// order_screen[0].style.display = 'none'
			merchant_screen[0].style.display = 'none'
			profile_screen[0].style.display = 'none'
	}

})

main_trigger.addEventListener('click', ()=>{
	// window.location.href = "/dashboard"
	main_screen[0].style.display = 'block'
	// document_upload_screen[0].style.display = "none"
	create_screen[0].style.display = 'none'
	// order_screen[0].style.display = 'none'
	merchant_screen[0].style.display = 'none'
	profile_screen[0].style.display = 'none'	
	current_screen = 1
})
profile_trigger.addEventListener('click', ()=>{
	main_screen[0].style.display = 'none'
	// document_upload_screen[0].style.display = "none"
	create_screen[0].style.display = 'none'
	// order_screen[0].style.display = 'none'
	merchant_screen[0].style.display = 'none'
	profile_screen[0].style.display = 'block'
	current_screen = 2
})
// document_upload_trigger.addEventListener('click', ()=>{
// // 	main_screen[0].style.display = 'none'
// 	document_upload_screen[0].style.display = "block"
// // 	create_screen[0].style.display = 'none'
// order_screen[0].style.display = 'none' 	
// // merchant_screen[0].style.display = 'none' 
// // profile_screen[0].style.display = 'none'
// // 	current_screen = 5
// })
create_trigger.addEventListener('click', ()=>{
	main_screen[0].style.display = 'none'
	// document_upload_screen[0].style.display = "none"
	create_screen[0].style.display = 'block'
	// order_screen[0].style.display = 'none'
	merchant_screen[0].style.display = 'none'
	profile_screen[0].style.display = 'none'
	current_screen = 3
})
merchant_trigger.addEventListener('click', ()=>{
	main_screen[0].style.display = 'none'
	// document_upload_screen[0].style.display = "none"
	create_screen[0].style.display = 'none'
	// order_screen[0].style.display = 'none'
	merchant_screen[0].style.display = 'block'
	profile_screen[0].style.display = 'none'
	current_screen = 3
})