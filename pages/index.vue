<script setup>
    import navbar from '~/components/navbar.vue';
    var config = useRuntimeConfig()
    const challenges = ref([])

    const searchString = ref("")
    const searchDifficulty = ref("any")
    const searchLanguage = ref("any")
    const currentPage = ref(0)


    async function search(text, difficulty, lang, page)
    {
        if (!text)
        {
            text = ""
        }
        var search_query = {text: text.toLowerCase(), difficulty: difficulty.toLowerCase(), lang: lang.toLowerCase(), page: page}
        var fetch = await useFetch("/api/search", {baseURL: config.public.apiBaseUrl, method: "POST", body: search_query})
        challenges.value = challenges.value.concat(fetch.data.value)
    }
    await search("", "any", "any", 0)

watch(searchString, async () => {challenges.value = []; currentPage.value = 0; await search(searchString.value, searchDifficulty.value, searchLanguage.value, currentPage.value)})
watch(searchDifficulty, async () => {challenges.value = []; currentPage.value = 0; await search(searchString.value, searchDifficulty.value, searchLanguage.value, currentPage.value)})
watch(searchLanguage, async () => {challenges.value = []; currentPage.value = 0; await search(searchString.value, searchDifficulty.value, searchLanguage.value, currentPage.value)})
watch(currentPage, async () => {await search(searchString.value, searchDifficulty.value, searchLanguage.value, currentPage.value)})


</script>

<template>
    <div class="flex w-full h-full justify-center flex-col">
        <navbar></navbar>
        <div class="flex w-full h-full py-10 px-48">
            <div class="w-full h-full card-color rounded-md">
                <div class="flex flex-row gap-10 p-3">
                    <div class="flex flex-row px-4 items-center">
                        <svg style="background-color: #ffffff1a; height: 100%;" xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 24 24" width="1em" height="1em" fill="#5e5e5e" class="w-4 h-4 rounded-l-md">
                            <path fill-rule="evenodd"
                                d="M5.527 5.527a7.5 7.5 0 0111.268 9.852l3.581 3.583a1 1 0 01-1.414 1.415l-3.582-3.583A7.501 7.501 0 015.527 5.527zm1.414 1.414a5.5 5.5 0 107.779 7.779A5.5 5.5 0 006.94 6.94z"
                                clip-rule="evenodd"></path>
                        </svg>
                        <input @change="searchString = $event.target.value" placeholder="Search" class="rounded-r-md rounded-l-none">
                    </div>
                    <div class="flex flex-row gap-2 items-center">
                        <p>Difficulty:</p>
                        <select @change="searchDifficulty = $event.target.value;">
                            <option value="any">Any</option>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                            <option value="6">6</option>
                            <option value="7">7</option>
                            <option value="8">8</option>
                        </select>
                    </div>
                    <div class="flex flex-row gap-2 items-center">
                        <p>Language:</p>
                        <select @change="searchLanguage = $event.target.value">
                            <option value="any">Any</option>
                            <option value="python">Python</option>
                            <option value="typescript">Typescript</option>
                            <option value="javascript">Javascript</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
        <div class="flex flex-col gap-3 w-full h-full px-48 mb-24">
            <NuxtLink v-for="challenge in challenges" :to="'/challenge?id=' + challenge._id">
            <div class="w-full card-color rounded-md p-5 flex flex-row cursor-pointer">
                <p class="w-96">{{ challenge.name }}</p>
                <p class="w-5">{{ challenge.difficulty }}</p>
                <div class="flex flex-row gap-5 grow pl-24">
                    <p v-for="lang in challenge.langs">
                        {{ lang }}
                    </p>
                </div>
            </div>
            </NuxtLink>
            <button class="card-color rounded-md text-white py-2 font-bold" @click="currentPage++">Load More</button>
        </div>
    </div>
</template>