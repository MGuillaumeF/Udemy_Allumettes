function askPlayer (alumettes, prece) {
  let result = 0;
  do {
    result = window.prompt("Combien d'alumette à retirer ?");
  } while (result < 1 || result > prece || result > alumettes);
  return result;
}

function askOrdi (alumettes, prece) {
  //let max = alumettes < prece ? alumettes : prece;
  //return Math.floor((Math.random() * max) + 1);
	if (alumettes <= 2 || prece == 2) {
		return 1;
	} else if ((alumettes - prece) >= (prece * 2 + 2) ) {
		return prece;
	} else if (alumettes === 3) {
		return 2;
	} else {
		return Math.floor((alumettes - 2) / 3) >= 1 ? Math.floor((alumettes - 2) / 3) : 1;
	}
}

function main (n) {
  var alumettes = n || Math.floor((Math.random() * Math.floor(90)) + 10);
  var prece = 2;
  var enter = 0;
  console.log("le jeu commence avec", alumettes, "alumettes");
  while (alumettes !== 0) {
    enter = askPlayer (alumettes, prece);
    prece = enter * 2;
    alumettes -= enter;
    
    console.log("Le joueur retire", enter, "alumettes");
    if (alumettes === 0) {
      console.log("le joueur perd");
      break;
    }
    console.log("il reste", alumettes, "alumettes");
    
    enter = askOrdi (alumettes, prece);
    prece = enter * 2;
    alumettes -= enter;
    console.log("L'ordinateur retire", enter, "alumettes");
    if (alumettes === 0) {
      console.log("l'ordinateur perd");
      break;
    }
    console.log("il reste", alumettes, "alumettes");
  }
  console.log("le jeu est terminé");
}

main(30);
