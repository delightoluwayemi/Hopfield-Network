""" if __name__ == "__main__":

    input= [[1,-1,-1,1]]
    state = [1,-1,-1,-1]
    node_count = len(state)
    sample_net = Hopfield_Network(node_count, input)
    energy = sample_net.update_energy()
    sample_net.train_network()
    sample_net.update_network_state(state) """

"""if __name__ == "__main__":

    new_image = image_processor("resources/patterns/pattern4_64x64.png")
    new_image.process_image()
    new_image.compress_array()
    new_image.plot_image(new_image.bipolar_conversion())"""