<script setup>

</script>

<template>
    <div class="flex w-full h-full justify-center flex-col">
        <div class="flex flex-row justify-start w-full h-14 card-color border-b-2 border-gray-500 px-24">
            <div class="flex flex-row items-center">
                <img class="h-full" src="/images/beet.png">
                <p class="font-bold">Beetcode</p>
            </div>
        </div>
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
                        <input placeholder="Search" class="rounded-r-md rounded-l-none">
                    </div>
                    <div class="flex flex-row gap-2 items-center">
                        <p>Difficulty:</p>
                        <select>
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
                        <select>
                            <option value="any">Any</option>
                            <option value="python">Python</option>
                            <option value="typescript">Typescript</option>
                            <option value="javascript">Javascript</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
        <div class="flex w-full h-full px-48">
            
        </div>
    </div>
</template>