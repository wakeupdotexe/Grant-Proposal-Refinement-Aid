import fs from 'fs';

const bannedWords = getData();

export function getData() {
    const file = fs.readFileSync('./bannedWords.txt', 'utf8')

    const allWords = file.toLowerCase().split('\n');

    for (let i = 0; i < allWords.length; i++) {
        allWords[i] = allWords[i].trim();
    }

    return allWords;
}


export function clickAction() {
    console.log('button clicked');
    let userProp = document.getElementById('user-input').value;
    //let recieved = wordSearch(userProp);
    document.getElementById('output')
        .innerText = userProp;
    
    console.log(userProp);
}

export function wordSearch(toSearch) {
    let foundWords = [];
    let revisedProp = toSearch.toLowerCase();
    for (let i = 0; i < bannedWords.length; i++) {
        const word = bannedWords[i];
        const pattern = new RegExp(word, 'gi');
        if (pattern.test(revisedProp)) {
            found = revisedProp.match(pattern);
            foundWords.push([word, found.length]);
            revisedProp = revisedProp.replace(pattern, '<strong>' + word + '</strong>');
        }
    }
    formatFoundWords(foundWords);
    return revisedProp;
}

export function formatFoundWords(foundWords) {
    for (let i = 0; i < foundWords.length; i++) {
        const word = foundWords[i][0];
        const count = foundWords[i][1];
        const listItem = document.createElement('li');
        listItem.innerHTML = `${word}: ${count}`;
        document.getElementById('output-list').appendChild(listItem);
    }

}