function goToRoute(route, method) {
	if (method[0] == 'GET') {
		window.location.pathname = route
	} else {
		var data = method[1]
		const url = `${window.location}${route}`
		fetch(url, {
			method: 'POST',
			headers: {'Content-Type': 'application/json'},
			body: JSON.stringify(data)
		})
		.then(response => response.text())
		.then(data => console.log(data))
	}
}