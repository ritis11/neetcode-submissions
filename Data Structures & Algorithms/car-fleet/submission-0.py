class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_dict = {}
        mono_stak = []
        for key, val in zip(position, speed):
            pos_speed_dict[key] = val
        sorted_pos = sorted(position, reverse=True)
        sorted_pos_speed = [pos_speed_dict[item] for item in sorted_pos]
        tim_array = [(target - pos)/s for pos, s in zip(sorted_pos,sorted_pos_speed)]
        mono_stak.append(tim_array[0])
        for ele in tim_array:
            mono_stak.append(mono_stak[-1]) if ele < mono_stak[-1] else mono_stak.append(ele)
        return len(set(mono_stak))

        