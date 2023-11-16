<script setup>
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
        <div class="flex w-full h-full py-10 px-12">
            <div class="flex grow">
                
            </div>
            <div class="flex grow">

            </div>
        </div>
    </div>
</template>