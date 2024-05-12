<x-app-layout>
    <x-slot name="header">
        <h2 class="font-semibold text-xl text-gray-800 leading-tight">
            {{ __('Search') }}
        </h2>
    </x-slot>

    <div class="py-12">
        <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
            <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-sm sm:rounded-lg">
                <div class="p-6 text-gray-900 dark:text-gray-100">
                    <form action="#" class="space-y-2 mb-6">
                        <div class="flex items-baseline space-x-2">
                            <x-select name="user_id" id="user_id" class="dark:bg-gray-200 dark:text-gray-800">
                                <option value="">All user</option>
                                @foreach($users as $user)
                                    <option value="{{ $user->id }}"
                                        {{ request()->get('user_id') == $user->id ? 'selected' : '' }}>
                                        {{ $user->name }}
                                    </option>
                                @endforeach
                            </x-select>

                            <x-input id="query" name="query" type="search" placeholder="Search for something ..."
                                     class="block w-full dark:bg-gray-800" value="{{ request()->get('query') }}"/>
                        </div>

                        <x-button class="dark:bg-gray-200 dark:text-gray-800">Search</x-button>
                    </form>

                    @if($results)
                        <div class="space-y-4">
                            @if($results->count())
                                <em>Found {{ $results->total() }} results</em>
                                @foreach($results as $result)
                                    <div>
                                        <h1 class="text-lg font-semibold">{{ $result->title }} #{{ $result->id }}</h1>
                                        <p>{{ $result->teaser }}</p>
                                        <p>{{ $result->user->name }}</p>
                                    </div>
                                @endforeach

                                {{ $results->links() }}
                            @else
                                <p>No results fund</p>
                            @endif
                        </div>
                    @endif
                </div>
            </div>
        </div>
    </div>
</x-app-layout>
