#!/usr/bin/node 
read arguments
const myList = arguments.split(' ')
if(myList.length == 0){
	console.log('No argument');
else if(myList.lenght == 1){
	console.log('Argument found');
else{
	console.log('Arguments found');
