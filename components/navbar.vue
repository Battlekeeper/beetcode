<script setup>
const props = defineProps(["signedIn"])
</script>

<template>
    <div class="flex flex-row justify-start w-full h-14 card-color border-b-2 border-gray-500">
        <NuxtLink to="/">
            <div class="flex flex-row items-center cursor-pointer h-full px-24 w-full">
                <img class="h-full select-none" src="/images/beet.png">
                <p class="font-bold select-none">Beetcode</p>
            </div>
        </NuxtLink>
        <div class="bg-yellow-400 rounded-b-lg px-5 py-1 flex flex-row gap-4 h-fit justify-self-center w-fit">
            <p class="text-black font-bold">Create an account to track your progress:</p>
            <button class="card-color text-white font-bold px-5 rounded-md">Join Now!</button>
        </div>
    </div>
    <LoadingIndicator>
        <div class="flex justify-center items-center backdrop-blur-lg"
            style="position: fixed; left: 0; top: 0; width: 100svw; height: 100svh;">
            <img src="/images/beet.png" class="w-1/12 animate-pulse ">
        </div>
    </LoadingIndicator>
</template>
<style></style>