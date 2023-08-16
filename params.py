from Parameters import Segmentation_Params, Reconstruction_Params

heart_params_seg = Segmentation_Params(delta = 8,
                                    GL_epsilon = 1e0,
                                    steps = 10,
                                    margin_proportion = 0.0225,
                                    maxiterations = 25,
                                    grad_Bhatt_MC = 1,
                                    Bhatt_MC = 2,#4
                                    sigma = 1e-2,
                                    beta = 2*1e2,
                                    gamma = 2*2*1e-2,#2*2*1e-2,
                                    momentum_u = 1e-5,
                                    threshold_seg = 0.25,
                                    max_sparsity_seg = 2000000,
                                   # max_sparsity_seg = 1000000,
                                    batch_size = 700,
                                    method = 'quadrature',
                                    dirac = 0,
                                    verbose = True)

brain_params_seg = Segmentation_Params(delta = 8,
                                    GL_epsilon = 1e0,
                                    steps = 10,
                                    margin_proportion = 0.1,
                                    maxiterations = 50,
                                    grad_Bhatt_MC = 10,
                                    Bhatt_MC = 25,
                                    sigma = 1e-2,
                                    beta = 2*1e4,
                                    gamma = 1e-3,
                                    momentum_u = 0,
                                    threshold_seg = 0.01,
                                    max_sparsity_seg = int(5*1e7),
                                    batch_size = 700,
                                    method = 'random',
                                    dirac = 0,
                                    verbose = True)

triangle_params_seg = Segmentation_Params(delta = 2,
                                    GL_epsilon = 1e0,
                                    steps = 100,
                                    margin_proportion = 0.05,
                                    maxiterations = 25,
                                    grad_Bhatt_MC = 10,
                                    Bhatt_MC = 50,
                                    sigma = 1e-2,
                                    beta = 2*1e2,
                                    gamma = 2*2*1e-2,
                                    momentum_u = 1e-5,
                                    threshold_seg = 0.01,
                                    max_sparsity_seg = 62500,
                                    batch_size = 700,
                                    method = 'random',
                                    dirac = 0,
                                    verbose = True)

rectangle_params_seg = Segmentation_Params(delta = 2,
                                    GL_epsilon = 1e0,
                                    steps = 100,
                                    margin_proportion = 0.05,
                                    maxiterations = 25,
                                    grad_Bhatt_MC = 10,
                                    Bhatt_MC = 50,
                                    sigma = 1e-2,
                                    beta = 2*1e2,
                                    gamma = 2*2*1e-2,
                                    momentum_u = 1e-5,
                                    threshold_seg = 0.01,
                                    max_sparsity_seg = 62500,
                                    batch_size = 700,
                                    method = 'random',
                                    dirac = 0,
                                    verbose = True)

recon_params = Reconstruction_Params(momentum_im = 1,
                                    sigma = 1e-2,
                                    batch_size = 700,
                                    alpha = 1,
                                    beta = 2*1e2,
                                    gfn_MC = 3,
                                    threshold_gfn = 3.5905,
                                    max_sparsity_gfn = 1000000,
                                    reg_a = 2e-1,
                                    reg_epsilon = 0.01,
                                    method = 'quadrature',
                                    verbose = True
                                    )


