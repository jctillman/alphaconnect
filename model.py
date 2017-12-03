import tensorflow as tf

class Connect4Model:

    def __init__(
            self,
            layers=[1,8,8,8,8,8,1]):

        self._make_variables(layers)

        self.X = tf.placeholder(tf.float32, shape=[None, 6, 7])
        self.Y = tf.placeholder(tf.float32, shape=[None, 1])

        self.X_reshaped = tf.reshape(self.X, shape=[-1, 6,7,1])

        self.output = self._make_calculations(self.X_reshaped, layers)
        self.loss = tf.losses.mean_squared_error(self.Y, self.output)
        self.optimizer = tf.train.RMSPropOptimizer(0.00001)
        self.trainer = self.optimizer.minimize(self.loss)

        init = tf.initialize_all_variables()
        self.saver = tf.train.Saver()
        self.sess = tf.Session()
        self.sess.run(init)

    def _make_variables(self, layers):
        self.vari = {}
        for n in range(len(layers)-1):
            conv = tf.Variable(
                    tf.random_normal(
                        [3, 3, layers[n], layers[n + 1]],
                        stddev=0.1, mean=0.0))
            bias = tf.Variable(tf.random_normal(
                        [ layers[n + 1] ],
                        stddev=0.1, mean=0.5))
            self.vari['conv' + str(n)] = conv
            self.vari['bias' + str(n)] = bias

    def _make_calculations(self, X, layers):
        
        prior_layer = X
        for n in range(len(layers)-1):
            conv = self.vari['conv' + str(n)]
            bias = self.vari['bias' + str(n)]
            layer = tf.layers.batch_normalization(prior_layer)
            layer = tf.nn.conv2d(layer, conv, strides=[1,1,1,1], padding='SAME')
            layer = layer + bias
            layer = tf.nn.elu(layer)
            prior_layer = layer

        shape = prior_layer.get_shape()
        amount = int(shape[1] * shape[2] * shape[3])
        ult_weight = tf.Variable(
                tf.random_normal(
                    [amount, 1],
                    stddev=0.1, mean=0.0))
        
        reshaped = tf.reshape(prior_layer, [-1, amount])
        return tf.sigmoid(tf.matmul(reshaped, ult_weight))


    def train(self, X,Y):

        input_stuff = {
            self.X: X,
            self.Y: Y,
        }
        loss, opt = self.sess.run([self.loss, self.trainer], feed_dict=input_stuff)
        return loss

    def use(self, X):
        pass
