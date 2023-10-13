#!/bin/bash

function marco() {
	export x="$PWD"
}

function polo() {
	cd "$x"
}
