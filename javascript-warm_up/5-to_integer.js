#!/usr/bin/node
const arg1 = process.argv.slice(2)[0]
if (Number(arg1) === NaN){
	console.log('Not a number');
}else{
	console.log(`My number: <${Number(arg1)}`);
}
