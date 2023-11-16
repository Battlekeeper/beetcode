<script setup>
import VueMarkdown from 'vue-markdown-render'
var config = useRuntimeConfig()
var route = useRoute()

var fetch = await useFetch("/api/challenge/" + route.query.id, { baseURL: config.public.apiBaseUrl })
var challenge = fetch.data.value
</script>

<template>
    <div class="flex w-full h-full justify-center flex-col">
        <div class="flex flex-row justify-start w-full h-14 card-color border-b-2 border-gray-500 px-24">
            <div class="flex flex-row items-center">
                <img class="h-full" src="/images/beet.png">
                <p class="font-bold">Beetcode</p>
            </div>
        </div>
        <div class="flex w-full h-full py-10 px-12 grow">
            <div class="flex w-1/2">
                <vue-markdown :source="challenge.description"></vue-markdown>
            </div>
            <div class="flex w-1/2">

            </div>
        </div>
    </div>
</template>

<style>
p
{
    white-space: normal;
}
h1 {
    font-size: 2em;
    font-family: Arimo, Helvetica, sans-serif;
    border-bottom: 2px solid #fafafa;
    margin-bottom: 1.15rem;
    padding-bottom: .5rem;
    text-align: center;
    color: white;
    font-weight: bolder;
    color: white;
}

h2 {
    font-size: 1.5em;
    font-family: Arimo, Helvetica, sans-serif;
    border-bottom: 2px solid #fafafa;
    margin-bottom: 1.15rem;
    padding-bottom: .5rem;
    text-align: center;
    color: white;
    font-weight: bolder;
    color: white;
}

h3 {
    font-size: 1.17em;
    font-family: Arimo, Helvetica, sans-serif;
    border-bottom: 2px solid #fafafa;
    margin-bottom: 1.15rem;
    padding-bottom: .5rem;
    text-align: center;
    color: white;
    font-weight: bolder;
    color: white;
}

h4 {
    font-size: 1em;
    font-family: Arimo, Helvetica, sans-serif;
    border-bottom: 2px solid #fafafa;
    margin-bottom: 1.15rem;
    padding-bottom: .5rem;
    text-align: center;
    color: white;
    font-weight: bolder;
    color: white;
}

h5 {
    font-size: .83em;
    font-family: Arimo, Helvetica, sans-serif;
    border-bottom: 2px solid #fafafa;
    margin-bottom: 1.15rem;
    padding-bottom: .5rem;
    text-align: center;
    color: white;
    font-weight: bolder;
    color: white;
}

h6 {
    font-size: .67;
    font-family: Arimo, Helvetica, sans-serif;
    border-bottom: 2px solid #fafafa;
    margin-bottom: 1.15rem;
    padding-bottom: .5rem;
    text-align: center;
    color: white;
    font-weight: bolder;
    color: white;
}



blockquote {
    border-left: 8px solid #fafafa;
    padding: 1rem;
}

pre,
code {
    background-color: #fafafa;
    color: black;
}

ul {
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    padding-inline-start: 40px;
    list-styletype: disc;
    margin-inline-start: 0;
    margin-inline-end: 0;
    margin-inline-start: 0;
    margin-inline-end: 0;
    counter-reset: list-item;
    list-style-image: none;
    list-style-position: outside;
    margin: 1em 0;
    padding: 0 0 0 30pt;
    color: white;
}
ol
{
    display: block;
    margin-block-start: 1em;
    margin-block-end: 1em;
    padding-inline-start: 40px;
    list-styletype: decimal;
    margin-inline-start: 0;
    margin-inline-end: 0;
    margin-inline-start: 0;
    margin-inline-end: 0;
    counter-reset: list-item;
    list-style-image: none;
    list-style-position: outside;
    margin: 1em 0;
    padding: 0 0 0 30pt;
}
li {
    display: list-item;
    text-align: match-parent;
    text-align: match-parent;
    text-align: match-parent;
    color: white;
}
</style>